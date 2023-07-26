from feast.feature_store import FeatureStore
from feast import Entity, FeatureView, Feature, ValueType, FileSource, Field
from datetime import timedelta
from feast import RepoConfig
from feast.repo_config import RegistryConfig

rc = RepoConfig(
    registry=RegistryConfig(
        registry_type="sql",
        path="mysql+pymysql://ufs_feast_rw:f2e230e6-d4a1-4441-8a97-71f729952d64@test-rds-mysql-egdataplatform-ufs-feast-registry-ins-0.cjesttwwup5d.us-east-1.rds.amazonaws.com:3306/ufs_feast",
        # path="mysql://ufs_feast_rw:f2e230e6-d4a1-4441-8a97-71f729952d64@test-aurora-mysql-egdataplatform-ufs-feast-reg.cluster-clz0epcefjqu.us-west-2.rds.amazonaws.com:3306/ufs_feast",
        cache_ttl_seconds=60
    ),
    project="feature_store",
    provider="local",
    offline_store="file",
    online_store="sqlite",
    entity_key_serialization_version=2,
)

store = FeatureStore(config=rc)

fvs = store.list_feature_views()
services = store.list_feature_services()
entities = store.list_entities()
sources = store.list_data_sources()

for s in sources:
    print("data source name", s.name)
    print("data source type", type(s))


for fv in fvs:
    print("fv name",fv.name)
    print("fv stream source", fv.stream_source)

    print("feature name",fv.features)
    print("entity_name", fv.entity_columns)

for s in services:
    print("service_name", s.name)
    print()
for e in entities:
    print("entity name",e.name)
