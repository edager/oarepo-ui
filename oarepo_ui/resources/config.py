import inspect
from pathlib import Path

import marshmallow as ma
from flask import current_app
from flask_resources import ResourceConfig
from invenio_base.utils import obj_or_import_string
from invenio_i18n.ext import current_i18n
from invenio_search_ui.searchconfig import FacetsConfig, SearchAppConfig, SortConfig


def _(x):
    """Identity function used to trigger string extraction."""
    return x


class UIResourceConfig(ResourceConfig):
    components = None
    template_folder = None

    def get_template_folder(self):
        if not self.template_folder:
            return None

        tf = Path(self.template_folder)
        if not tf.is_absolute():
            tf = (
                Path(inspect.getfile(type(self)))
                .parent.absolute()
                .joinpath(tf)
                .absolute()
            )
        return str(tf)

    response_handlers = {"text/html": None}
    default_accept_mimetype = "text/html"

    # Request parsing
    request_read_args = {}
    request_view_args = {}


class RecordsUIResourceConfig(UIResourceConfig):
    routes = {
        "search": "",
        "create": "/_new",
        "detail": "/<pid_value>",
        "edit": "/<pid_value>/edit",
        "export": "/<pid_value>/export/<export_format>",
    }
    request_view_args = {"pid_value": ma.fields.Str()}
    request_export_args = {"export_format": ma.fields.Str()}

    app_contexts = None
    ui_serializer = None
    ui_serializer_class = None

    api_service = None
    """Name of the API service as registered inside the service registry"""

    templates = {
        "detail": {
            "layout": "oarepo_ui/detail.html",
        },
        "search": {
            "layout": "oarepo_ui/search.html",
        },
        "edit": {"layout": "oarepo_ui/form.html"},
        "create": {"layout": "oarepo_ui/form.html"},
    }
    layout = "sample"

    empty_record = {}

    @property
    def exports(self):
        return {
            "json": {
                "name": _("JSON"),
                "serializer": ("flask_resources.serializers:JSONSerializer"),
                "content-type": "application/json",
                "filename": "{id}.json",
            },
        }

    @property
    def ui_serializer(self):
        return obj_or_import_string(self.ui_serializer_class)()

    def search_available_facets(self, api_config, identity):
        return api_config.search.facets

    def search_available_sort_options(self, api_config, identity):
        return api_config.search.sort_options

    def search_active_facets(self, api_config, identity):
        return list([])

    def search_active_sort_options(self, api_config, identity):
        return list(api_config.search.sort_options.keys())

    def search_sort_config(
        self,
        available_options,
        selected_options=[],
        default_option=None,
        no_query_option=None,
    ):
        return SortConfig(
            available_options, selected_options, default_option, no_query_option
        )

    def search_facets_config(self, available_facets, selected_facets=[]):
        facets_config = {}
        for facet_key, facet in available_facets.items():
            facets_config[facet_key] = {
                "facet": facet,
                "ui": {
                    "field": facet._params.get("field", facet_key),
                },
            }

        return FacetsConfig(facets_config, selected_facets)

    def search_app_config(self, identity, api_config, overrides=None, **kwargs):
        opts = dict(
            endpoint=f"/api{api_config.url_prefix}",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            grid_view=False,
            sort=self.search_sort_config(
                available_options=self.search_available_sort_options(
                    api_config, identity
                ),
                selected_options=self.search_active_sort_options(api_config, identity),
            ),
            facets=self.search_facets_config(
                available_facets=self.search_available_facets(api_config, identity),
                selected_facets=self.search_active_facets(api_config, identity),
            ),
        )
        opts.update(kwargs)
        overrides = overrides or {
            "ui_endpoint": self.url_prefix,
        }
        return SearchAppConfig.generate(opts, **overrides)

    @property
    def custom_fields(self):
        # TODO: currently used by forms only, implement custom fields loading
        return {
            "ui": {},
        }

    def languages_config(self, identity):
        return dict(
            common=[],
            all=[]
        )

    def form_config(self, identity=None, **kwargs):
        """Get the react form configuration."""
        conf = current_app.config

        return dict(
            current_locale=str(current_i18n.locale),
            locales=[
                {"value": l.language, "text": l.get_display_name()}
                for l in current_i18n.get_locales()
            ],
            default_locale=conf.get("BABEL_DEFAULT_LOCALE", "en"),
            languages=self.languages_config(identity),
            links=dict(),
            custom_fields=self.custom_fields,
            **kwargs,
        )
