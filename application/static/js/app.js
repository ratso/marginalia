$(function() {
	$("textarea.note-body").qeditor({});

	$('a.note-controls').bind({
		mouseenter: function(e) {

		},
		mouseleave: function(e) {

		},
		blur: function(e) {
			// Blur event handler
		}
	});

	$('a.note-del-btn').bind('click', function() {
		var href = $(this).attr('href');
		if (!$('#dataConfirmModal').length) {
			$('body').append('');
		}
		$('#dataConfirmModal').find('.modal-body').text($(this).attr('data-confirm'));
		$('#dataConfirmOK').attr('href', href);
		$('#dataConfirmModal').modal({show:true});
		return false;
	});

	$('a.note-edit-btn').bind('click', function() {
		var sId = $(this).closest('div.panel').get(0).getAttribute('id');
		var Id = parseInt(sId.slice(2));
		console.log(sId);
	})
});

var app = {};

app.Notes = Backbone.Model.extend({
      url: '/getNotes',
    initialize:function(params){
    },
    getNotes: function(path){
        return this.fetch({
            contentType: 'application/json',
            type: 'GET', //здесь можно писать и GET и POST
            cache:false,
            url:this.url
        });
    }
    });

// instance of the Collection
    app.NotesList = new app.Notes();

    app.NotesView = Backbone.View.extend({
      tagName: 'li',
      template: _.template($('#item-template').html()),
      render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        return this; // enable chained calls
      }
    });

app.AppView = Backbone.View.extend({
      el: '#application',
      initialize: function () {
        this.input = this.$('#new-todo');
        // when new elements are added to the collection render then with addOne
        app.NotesList.getNotes(); // Loads list from local storage
      },
      addOne: function(todo){
        var view = new app.NotesView({model: todo});
        $('#todo-list').append(view.render().el);
        console.log('111');
      },
      addAll: function(){
        this.$('#todo-list').html(''); // clean the todo list
        app.todoList.each(this.addOne, this);
        console.log('222');
      },
      newAttributes: function(){
        return {
          title: this.input.val().trim(),
          completed: false
        }
      }
    });

    //--------------
    // Initializers
    //--------------

    app.appView = new app.AppView();