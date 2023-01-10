from ad_unit.models import AdUnit


def create_ad_unit_filter_dict(query_params: dict = None) -> dict:

    updated_dict = {}
    query_params = query_params or {}
    valid_keys = {f.name for f in AdUnit._meta.get_fields()}

    for key, value in query_params.items():
        if key.lower() not in valid_keys:
            raise KeyError(f"{key} is not valid")
        new_key = f"targeting__{key}"
        updated_dict[new_key] = str(value.title())

    return updated_dict
