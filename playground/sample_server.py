from flask import Flask

from oarepo_ui.ext import OARepoUIExtension
from oarepo_ui.default_ui_extension import DefaultUIExtensionConfig
from oarepo_ui.resources.templating import render_template_with_macros
from oarepo_ui.views import blueprint

from importlib_resources import files as import_files

app = Flask('sample_server', template_folder='templates')
app.config["TEMPLATES_AUTO_RELOAD"] = True
OARepoUIExtension(app)
ext = app.extensions["oarepo_ui"]
ext.ui_extensions.append(DefaultUIExtensionConfig(app))
app.register_blueprint(blueprint)

record = {"id": "qq28e-k8m51", "updated": "2022-03-12", "created": "2022-03-12",
          "metadata": {"resourceType": "Diplomov\u00e1 pr\u00e1ce", "accessibility": [
              {"value": "Dostupn\u00e9 v digit\u00e1ln\u00edm repozit\u00e1\u0159i UK.", "lang": "cs"},
              {"value": "Available in the Charles University Digital Repository.", "lang": "en"}],
                       "dateIssued": "2022-02-01", "contributors": [
                  {"nameType": "Personal", "fullName": "Hodbo\u010f, Vojt\u011bch", "role": "advisor"},
                  {"nameType": "Personal", "fullName": "Soukup, Martin", "role": "referee"}], "languages": ["cs"],
                       "collection": "Univerzita Karlova",
                       "degreeGrantor": ["Univerzita Karlova", "Katedra medi\u00e1ln\u00edch studi\u00ed",
                                         "Fakulta soci\u00e1ln\u00edch v\u011bd"],
                       "title": "Sebereflexe vlastn\u00ed medi\u00e1ln\u00ed zku\u0161enosti s chytr\u00fdm telefonem jako rozvoj medi\u00e1ln\u00ed gramotnosti: autoetnografie",
                       "subjects": [
                           {"subjectScheme": "keyword", "subject": [{"value": "self-reflection", "lang": "en"}]},
                           {"subjectScheme": "keyword", "subject": [{"value": "autoethnography", "lang": "en"}]},
                           {"subjectScheme": "keyword", "subject": [{"value": "media literacy", "lang": "en"}]},
                           {"subjectScheme": "keyword", "subject": [{"value": "media experience", "lang": "en"}]},
                           {"subjectScheme": "keyword", "subject": [{"value": "smartphone", "lang": "en"}]},
                           {"subjectScheme": "keyword", "subject": [{"value": "sebereflexe", "lang": "cs"}]},
                           {"subjectScheme": "keyword", "subject": [{"value": "autoetnografie", "lang": "cs"}]},
                           {"subjectScheme": "keyword",
                            "subject": [{"value": "medi\u00e1ln\u00ed gramotnost", "lang": "cs"}]},
                           {"subjectScheme": "keyword",
                            "subject": [{"value": "medi\u00e1ln\u00ed zku\u0161enost", "lang": "cs"}]},
                           {"subjectScheme": "keyword",
                            "subject": [{"value": "chytr\u00fd telefon", "lang": "cs"}]}], "abstract": [{
                  "value": "The subject of this autoethnography is the self-reflection of my own media experience, which I experience daily with a smartphone. The aim of the work is to discover my intimate and individual media experience with the most used technology and to see how this professional self-reflection can lead to the development of media literacy. Current times and society are changing ever more rapidly due to technological developments, which is why we need to adapt to these changes individually throughout our lives. The first part of the thesis thus describes theoretical basis concerning media literacy and self-reflection in the context of post-modern times, the current approach to media education, the concept of dynamic lifelong learning and the new, transformative competences needed for a happy life in the 21st century. The second part of the thesis explains the qualitative methodological process of autoethnography and data collection, which took place over six months through a self-reflective journal. The final part of the work uncovers thematic categories gained from the data set, in which I deconstructed that a smartphone means for me above all security, health, ambivalence, self-fulfilment, but overall the satisfaction of these needs. I noticed that I changed the way of thinking, my opinions, behaviour, emotions,...",
                  "lang": "en"},
                  {
                      "value": "P\u0159edm\u011btem t\u00e9to autoetnografie je sebereflexe vlastn\u00edch medi\u00e1ln\u00edch zku\u0161enost\u00ed, kter\u00e9 dennodenn\u011b za\u017e\u00edv\u00e1m s chytr\u00fdm telefonem. C\u00edlem pr\u00e1ce je objevit svoji intimn\u00ed a individu\u00e1ln\u00ed medi\u00e1ln\u00ed zku\u0161enost a zjistit, jak tato odborn\u00e1 sebereflexe m\u016f\u017ee v\u00e9st k rozvoji medi\u00e1ln\u00ed gramotnosti. Sou\u010dasn\u00e1 doba i spole\u010dnost se kv\u016fli technologick\u00e9mu v\u00fdvoji m\u011bn\u00ed \u010d\u00edm d\u00e1l t\u00edm rychleji, a proto je t\u0159eba se t\u011bmto zm\u011bn\u00e1m p\u0159izp\u016fsobovat individu\u00e1ln\u011b po cel\u00fd \u017eivot. Prvn\u00ed \u010d\u00e1st pr\u00e1ce tak popisuje teoretick\u00e1 v\u00fdchodiska t\u00fdkaj\u00edc\u00ed se medi\u00e1ln\u00ed gramotnosti a sebereflexe v kontextu postmodern\u00ed doby, sou\u010dasn\u00e9ho p\u0159\u00edstupu k medi\u00e1ln\u00ed v\u00fdchov\u011b, konceptu dynamick\u00e9ho celo\u017eivotn\u00edho vzd\u011bl\u00e1v\u00e1n\u00ed (lifelong learning) a nov\u00fdch, transformativn\u00edch kompetenc\u00ed pot\u0159ebn\u00fdch pro spokojen\u00fd \u017eivot ve 21. stolet\u00ed. Druh\u00e1 \u010d\u00e1st pr\u00e1ce objas\u0148uje kvalitativn\u00ed metodick\u00fd postup autoetnografie a sb\u011br dat, kter\u00fd prob\u00edhal po dobu \u0161esti m\u011bs\u00edc\u016f skrze sebereflektivn\u00ed den\u00edk. Z\u00e1v\u011bre\u010dn\u00e1 \u010d\u00e1st pr\u00e1ce odkr\u00fdv\u00e1 tematick\u00e9 kategorie ze z\u00edskan\u00fdch dat, ve kter\u00fdch jsem rozkl\u00ed\u010dovala, \u017ee chytr\u00fd telefon pro m\u011b znamen\u00e1 p\u0159edev\u0161\u00edm jistotu, zdrav\u00ed, rozpolcenost, seberealizaci, ale celkov\u011b uspokojen\u00ed t\u011bchto pot\u0159eb. Z\u00e1rove\u0148 se uk\u00e1zalo, \u017ee je pot\u0159eba dal\u0161\u00edch v\u00fdzkum\u016f v oblasti sebereflexe, akcentuj\u00edc\u00ed kognitivn\u00ed, emoci\u00e1ln\u00ed a behavior\u00e1ln\u00ed procesy u jedince, a jej\u00edho vlivu v rozvoji medi\u00e1ln\u00ed gramotnosti.",
                      "lang": "cs"}],
                       "originalRecord": "http://hdl.handle.net/20.500.11956/171594",
                       "systemIdentifiers": [{"scheme": "nusl", "identifier": "http://www.nusl.cz/ntk/nusl-456298"},
                                             {"scheme": "originalRecordOAI",
                                              "identifier": "oai:https://dspace.cuni.cz:20.500.11956/171594"},
                                             {"scheme": "nuslOAI", "identifier": "oai:invenio.nusl.cz:456298"}],
                       "defended": True, "additionalTitles": [{"title": [{
                  "value": "Self-reflection of my own media experience with a smartphone as a development of media literacy: autoetnography",
                  "lang": "en"}],
                  "titleType": "translatedTitle"}],
                       "accessRights": "otev\u0159en\u00fd p\u0159\u00edstup",
                       "creators": [{"fullName": "Veberov\u00e1, Kl\u00e1ra", "nameType": "Personal"}],

                       # just for debugging/demo
                       'list_of_strings': [
                           "first string",
                           "second string",
                           "third string",
                       ]
                       },
          "links": {"self": "/api/nr_theses_metadata/qq28e-k8m51"}}

row_layout = [
    {
        "component": "grid",
        "className": "demo",
        "columnsPerRow": 2,
        "rows": [
            {
                "columns": [
                    {
                        "component": "placeholder",
                    },
                    {
                        "component": "placeholder",
                    }
                ]
            },
            {
                "columns": [
                    {
                        "component": "column",
                        "className": "ten wide",
                        "items": [
                            {
                                "component": "placeholder",
                            }
                        ]
                    },
                    {
                        "component": "placeholder",
                    }
                ]
            }
        ]
    }
]

column_layout = [
    {
        "component": "grid",
        "columnsPerRow": 2,
        "className": "demo",
        "columns": [
            {
                "component": "placeholder",
            },
            {
                "component": "placeholder",
            }
        ]
    }
]

icon_name_layout = [
    {
        'component': 'icon',
        'name': "thumbs up",
        "color": "green",
        "size": "large"
    }
]

icon_iconset_layout = [
    {
        'component': 'icon',
        'name': "thup",
        "color": "green",
        "size": "large",
        "iconSet": {
            "thup": "thumbs up"
        }
    },
    {
        'component': 'icon',
        'name': "thdn",
        "color": "green",
        "size": "large",
        "iconSet": {
            "thdn": {
                'name': "thumbs down",
                "color": "red"
            }
        }
    }
]

icon_image_layout = [
    {
        'component': 'icon',
        "size": "mini",
        "src": "https://semantic-ui.com//images/wireframe/image.png"
    }
]

icon_data_name_layout = [
    {
        'component': 'icon',
        'dataField': 'accessRights',
        "color": "green",
        "size": "large",
        "iconSet": {
            "otev\u0159en\u00fd p\u0159\u00edstup": "thumbs up"
        }
    }
]

icon_data_image_layout = [
    {
        'component': 'icon',
        'dataField': 'accessRights',
        "color": "green",
        "size": "mini",
        "iconSet": {
            "otev\u0159en\u00fd p\u0159\u00edstup": {
                "src": "https://semantic-ui.com//images/wireframe/image.png"
            }
        }
    }
]

list_layout = [
    {
        'component': 'list',
        'dataField': 'list_of_strings'
    }
]

horizontal_list_layout = [
    {
        'component': 'list',
        'horizontal': True,
        'dataField': 'list_of_strings'
    }
]

horizontal_list_with_separator_layout = [
    {
        'component': 'list',
        'horizontal': True,
        'dataField': 'list_of_strings',
        'separator': ', '
    }
]

horizontal_list_with_separator_component_layout = [
    {
        'component': 'list',
        'horizontal': True,
        'dataField': 'list_of_strings',
        'separator': {'component': 'separator'}
    }
]

separator_layout = [
    {
        'component': 'raw',
        'data': "Hello",
    },
    {
        'component': 'separator'
    },
    {
        'component': 'raw',
        'data': "World",
    },
    {
        'component': 'separator',
        'double': True,
        'color': 'green'
    },
    {
        'component': 'raw',
        'data': "How are you?",
    }
]

divided_row = [
    {
        'component': 'divided-row',
        'separator': {
            'component': 'separator',
            'color': 'green'
        },
        'items': [
            {
                'component': 'raw',
                'data': "Hello",
            },
            {
                'component': 'raw',
                'data': "World",
            },
            {
                'component': 'raw',
                'data': " ",  # whitespace should not be rendered
            },
            {
                'component': 'raw',
                'data': "How are you?",
            }
        ]
    }
]

button = [
    {
        "component": "button",
        "dataField": "resourceType"
    }
]

container = [
    {
        "component": "container",
        "dataField": "abstract.value",
        "className": "text"
    }
]

header = [
    {
        "component": "header",
        "element": "h1",
        "content": "H1 header"
    },
    {
        "component": "header",
        "element": "h2",
        "content": "H2 header"
    },
    {
        "component": "header",
        "element": "h3",
        "content": "H3 header"
    },
    {
        "component": "header",
        "element": "h4",
        "content": "H4 header"
    },
    {
        "component": "header",
        "element": "h5",
        "content": "H5 header"
    },
    {
        "component": "header",
        "element": "h6",
        "content": "H6 header"
    },
    {
        "component": "header",
        "content": "Huge header",
        "className": "huge"
    },
    {
        "component": "header",
        "content": "Large header",
        "className": "large"
    },
    {
        "component": "header",
        "content": "Medium header",
        "className": "medium"
    },
    {
        "component": "header",
        "content": "small header",
        "className": "small"
    },
    {
        "component": "header",
        "content": "tiny header",
        "className": "tiny"
    },
]

label = [
    {
        "component": "label",
        "content": "label content",
    },
    {
        "component": "label",
        "dataField": "resourceType",
    }
]

link = [
    {
        "component": "link",
        "content": "Go to google !!!",
        "href": "https://google.com"
    },
    {
        "component": "link",
        "content": "Go to original record !!!",
        "dataField": "originalRecord"
    }
]

segment = [
    {
        "component": "segment",
        "dataField": "abstract.value",
    },
    {
        "component": "segment",
        "content": "Blah blah",
    }
]

span = [
    {
        "component": "span",
        "dataField": "originalRecord",
    },
    {
        "component": "span",
        "content": "Blah blah",
    }
]

@app.route('/')
def index():
    extra_css = import_files('oarepo_ui.css').joinpath('builtin.css').read_text()
    return render_template_with_macros(
        'sample_server.html.jinja2',
        record=record,
        data=record['metadata'],
        extra_css=extra_css,
        layouts={
            'Simple grid with two columns': column_layout,
            'Simple grid with two rows': row_layout,
            'Normal icon with name': icon_name_layout,
            'Normal icon with image': icon_image_layout,
            'Icon with iconSet': icon_iconset_layout,
            'Normal icon with data-driven name': icon_data_name_layout,
            'Normal icon with data-driven image': icon_data_image_layout,
            'Simple list': list_layout,
            'Simple horizontal list': horizontal_list_layout,
            'Simple horizontal list with separator': horizontal_list_with_separator_layout,
            'Simple horizontal list with separator component': horizontal_list_with_separator_component_layout,
            'Separator': separator_layout,
            'Divided row': divided_row,
            'Button': button,
            'Container with text': container,
            'Header': header,
            'Label': label,
            'Link': link,
            'Segment': segment,
            'Span': span,
        }
    )


if __name__ == '__main__':
    app.run(debug=True)