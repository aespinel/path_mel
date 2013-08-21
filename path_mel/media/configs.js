define([],
function() {
    
    /*
    var dummy_config = {
        entity_name : 
        //string = key of this object in all_config, name of objectstore in IDB
        //for - accessing this object 
        
        'rest_api_url': '/coco/api/v1/village/',
        //string - the rest url for this entity
    
        'dashboard_display': {
            listing: false,         //whether to provide listing option for this entity on dashboard
            add: false              //whether to provide add option for this entity on dashboard
        },
    
        -----------------------------------Listing configs---------------------------------
        page_header: 'Village',  
        //string = The name that needs to shown in headers 

        list_table_header_template: 'village_table_template',  
        //HTML template - The id of template used as coloumn headers in list page

        list_table_row_template: 'village_list_item_template',  
        //HTML template - The id of template used to create rows of list table. 
        //This template is passed the model json.
        -----------------------------------------------------------------------------------
    
        ----------------------------------Form configs-------------------------------------
        foreign_entities: {
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'placeholder': 'string - the id of element in form's html where the dropdown of this f_entity is inserted',
                    
                    'name_field': 'string - the attribute name in f_entity's json which needs to be shown in its dropdown',
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                        'src_attr' : //to compare dep_attr of dependent element with a particular attribute in source f_entity
                    }],
                    
                    'filter': { //whether to filter the objects of foreign entity before rendering into dropdown
                        attr: 'group',  //the attribute name in f_entity's json to filter on
                        value: null     //desired value of the attr
                    },
    
                    id_field: "person_id", // the name of id field for this f_entity in denormalised json                         
                }
            },
    
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                    }],

                    id_field: "person_id", // the name of id field for this f_entity in denormalised json     

                    //would not use options template to render its objects - would use the specfied template    
                    // won't be denormalised, wud be converted offline to online, 
                    //any field to be denormalised or converted offline to online can be declared - 
                    //this shd be clubbed and put as foreign entity of expanded.   
                    'expanded': { 
                        template: 'person_pma_template', // the template to use instead of options
                        placeholder: 'pmas',    // the id of placeholder in form's HTML
                        TODO: the following two should be merged and converted to same format as foreign_entities
                        denormalize: { // any field in expanded template to be denormalised     
                            "expressed_adoption_video": {
                                name_field: 'title' //used as key for name in denormalised object
                            }
                        },
                        foreign_fields: { // any more field in expanded template for offline to online conv
                            "expressed_adoption_video": {
                                entity_name: "video"  //the entity_name for this f_entity element
                            }
                        },
                        extra_fields: ["expressed_question", "interested", "expressed_adoption_video"]
                    }
                }
            }
        },    
        //object - describes the foreign keys in the json of this entity's model.
        //To convert between online offline namespaces, denormalize-normalize json    
    
        inline: {
            'entity': 'person',     //entity name of inline
    
            'default_num_rows': 10,         //default num of rows to show
    
            "template": "person_inline",    //id of template used to render inline
            //Include any jquery validation desired inside html of rows 
            //TODO: need to explain the <%index%> tags required in inlines
    
            "foreign_attribute": {
                'host_attribute': ["id", "group_name"],
                'inline_attribute': "group"
            },
            "header": "person_inline_header",
            'borrow_attributes': [{
                'host_attribute': 'village',
                'inline_attribute': 'village'
            }]
        },      
        //object - describes inlines to be included in this entity's form

        bulk:{},     
        //object - if multiple objects of this entity type can be saved through its add form, describe configs of object 
        ------------------------------------------------------------------------------------
    }
    */
    
    // //This template would be passed the json of inline model and shall produce the desired row
//     TODO: maybe instead of relying on users to use templating lang we should fill the rows ourselves in js code, like we are doing in form!

    var village_configs = {
        'page_header': 'Village',
        'add_template_name': 'village_add_edit_template',
        'edit_template_name': 'village_add_edit_template',
        'list_table_header_template': 'village_table_template', 
        'list_table_row_template': 'village_list_item_template',
        'rest_api_url': '/coco/api/v1/village/',
        'entity_name': 'village',
        'sort_field': 'name'
    };

    var mediator_configs = {
        'page_header': 'Mediator',
        'list_table_header_template': 'mediator_table_template',
        'list_table_row_template': 'mediator_list_item_template',
        'add_template_name': 'mediator_add_edit_template',
        'edit_template_name': 'mediator_add_edit_template',
        'rest_api_url': '/coco/api/v1/mediator/',
        'entity_name': 'mediator',
        'unique_together_fields': ['name'],
        'sort_field': 'name',
        'foreign_entities': {
            'village': {
                "villages": {
                    'placeholder': 'id_villages',
                    'name_field': 'name'
                }, //name of html element in form/ attribute name in json: {placeholder: "id of html element in form", name_field: "attribute in foreign entity's json "} 
            },
        },
        'form_field_validation': {
            ignore: [],
            rules: {
                name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    allowedChar: true
                },
                villages: "required",
            },
            messages: {
                name: {
                    required: 'Mediator name is required',
                    minlength: 'Mediator name should contain at least 2 characters',
                    maxlength: 'Mediator name should contain at most 100 characters',
                    allowedChar: 'Mediator name should contain only english and local language characters'
                },
                villages: "Villages are required",
            },

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline"

        }

    };

    var video_configs = {
        'page_header': 'Video',
        'list_table_header_template': 'video_table_template',
        'list_table_row_template': 'video_list_item_template',
        'add_template_name': 'video_add_edit_template',
        'edit_template_name': 'video_add_edit_template',
        'rest_api_url': '/coco/api/v1/video/',
        'entity_name': 'video',
        'unique_together_fields': ['title'],
        'sort_field': 'title',
        'form_field_validation': {
            ignore: [],
            rules: {
                title: {
                    required: true,
                    minlength: 2,
                    maxlength: 200,
                    // allowedChar: true
                },
            },
            messages: {
                title: {
                    required: 'Video title is required',
                    minlength: 'Video title should contain at least 2 characters',
                    maxlength: 'Video title should contain at most 200 characters',
                    // allowedChar: 'Video title should only contain alphabets and local language characters'
                },
            },

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline"

        }
    };
    
    var dissemination_configs = {
        'page_header': 'Dissemination',
        'list_table_header_template': 'dissemination_table_template',
        'list_table_row_template': 'dissemination_list_item_template',
        'add_template_name': 'dissemination_add_edit_template',
        'edit_template_name': 'dissemination_add_edit_template',
        'rest_api_url': '/coco/api/v1/dissemination/',
        'entity_name': 'dissemination',
        download_chunk_size: 1000,
        'unique_together_fields': ['date', 'start_time', 'end_time', 'village.id', 'mediator.id'],
        'foreign_entities': {
            'village': {
                'village': {
                    'placeholder': 'id_village',
                    'name_field': 'name'
                },
            },
            'video': {
                'video': {
                    'placeholder': 'id_video',
                    'name_field': 'title'
                },
            },
            'mediator': {
                'mediator': {
                    'placeholder': 'id_mediator',
                    'name_field': 'name',
                    'dependency': [{
                        'source_form_element': 'village',
                        'dep_attr': 'villages'
                    }]
                }
            },
            'person': {
                attendance_records: {
                    dependency: [{
                        'source_form_element': 'village',
                        'dep_attr': 'village'
                    }],
                    id_field: "person_id", // for convert_namespace conversion      
                    'expanded': { // won't be denormalised, wud be converted offline to online, render wud use a template declared and nt options template, any field to be denormalised or converted offline to online can be declared - this shd be clubbed and put as foreign entity of expanded.  
                        template: 'person_pma_template',
                        placeholder: 'attendance_records',
                        extra_fields: ["question_asked", "interested"]
                    }
                }
            }
        },
        'form_field_validation': {
            ignore: [],
            rules: {
                date: {
                    required: true,
                    validateDate: true
                },
                start_time: {
                    required: true,
                    validateTime: true
                },
                end_time: {
                    required: true,
                    validateTime: true,
					timeOrder: {start_time : "start_time"}
                },
                mediator: "required",
                village: "required",
                video: "required",

            },
            messages: {
				date: {
					required: 'Date is required',
					validateDate: 'Enter date in the form of YYYY-MM-DD',
				},
				start_time: {
					required: 'Start time is required',
					validateTime: 'Enter the start time in the form of HH:MM. Use 24 hour format',
				},
				end_time: {
					required: 'End time is required',
					validateTime: 'Enter the end time in the form of HH:MM. Use 24 hour format',
					timeOrder: 'End time should be later than start time',
				},
				mediator: "Mediator is required",
				village:"Village is required",
				videoes_screened:"Video is required",
			},

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline"
        }
    };
    
    var adoption_configs = {
        'page_header': 'Adoption',
        'list_table_header_template': 'adoption_table_template',
        'list_table_row_template': 'adoption_list_item_template',
        'add_template_name': 'adoption_add_template',
        'edit_template_name': 'adoption_edit_template',
        'rest_api_url': '/coco/api/v1/adoption/',
        'entity_name': 'adoption',
        'inc_table_name': 'adoption',
        'unique_together_fields': ['person.id', 'date'],
        form_field_validation: {
            ignore: [],
            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-block",
            display: "block"
        },
        
        'foreign_entities': {
            'village': {
                'village': {
                    'placeholder': 'id_village',
                    'name_field': 'name'
                },
            },
            'person': {
                    'placeholder': 'id_person',
                    'name_field': 'name',
                    'dependency': [{
                        'source_form_element': 'village',
                        'dep_attr': 'village'
                    }],
                },
            'mediator': {
                'placeholder': 'id_mediaAdoptionResourcetor',
                'name_field': 'name',
                'dependency': [{
                    'source_form_element': 'village',
                    'dep_attr': 'villages'
                }],
            }
        }
    };
    
    
    var person_configs = {
        'page_header': 'Person',
        'list_table_header_template': 'person_table_template',
        'list_table_row_template': 'person_list_item_template',
        'add_template_name': 'person_add_edit_template',
        'edit_template_name': 'person_add_edit_template',
        'rest_api_url': '/coco/api/v1/person/',
        'entity_name': 'person',
        'foreign_entities': {
            'village': {
                'village': {
                    'placeholder': 'id_village',
                    'name_field': 'name'
                },
            },
        },
        'unique_together_fields': ['name', 'other_name', 'village.id'],
        'sort_field': 'name',
        'form_field_validation': {
            ignore: [],
            rules: {
                name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar:true
                },

                other_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar:true
                },
                age: {
                    digits: true,
                    min: 1,
                    max: 100
                },
                gender: "required",
                village: {
                    required: true
                }
            },
            messages: {
				name: {
					required: 'Name is required',
					minlength: 'Name  should contain at least 2 characters',
					maxlength: 'Name should contain at most 100 characters',
					allowedChar: 'Name should contain only english and local language characters'
				},
				other_name: {
					required: "Other name is required",
					minlength: "Other name should contain at least 2 characters",
					maxlength: "Other name should contain at most 100 characters",
					allowedChar: "Other name should contain only english and local language characters"
				},
				age: {
					digits: "Age should contain only digits",
					min:"Age should not be less than 1 year",
					max:"Age should not be more than 100 years"
				},
				gender:{
					required: "Gender is required"
				},
				village: {
					required: "Village is required"
				}
			},

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline"
        }

    };
    
    var misc = {
        download_chunk_size: 2000,
        background_download_interval: 1 * 60 * 1000,
        inc_download_url: "get_log/",
    };

    return {
        village: village_configs,
        mediator: mediator_configs,
        video: video_configs,
        person: person_configs,
        dissemination: dissemination_configs,
        adoption: adoption_configs,
        misc: misc
    }

});
