from .es_template import ElasticSearchTemplate

class GenericItemStore(ElasticSearchTemplate):
    INDEX = "generic_items"

    MAPPING = {
        "mappings": {
            "generic_items": {
                "properties": {
                    "name": { "type" : "text" },
                    "class": { "type" : "text" },
                    "base_item": { "type" : "text" },
                    "implicit_stat_text": { "type" : "text" },
                    "explicit_stat_text": { "type" : "text" },
                    "drop_level": { "type" : "integer" },
                    "drop_level_maximum": { "type" : "integer" },
                    "required_dexterity": { "type" : "integer" },
                    "required_intelligence": { "type" : "integer" },
                    "required_level": { "type" : "integer" },
                    "required_level_base": { "type" : "integer" },
                    "required_strength": { "type" : "integer" },
                    "base_item": { "type" : "text" },
                }
            }
        }
    }
