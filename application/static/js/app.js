// Global application object
var app = {};

// Utils
app.tools = {};

app.tools.validateEmail = function(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
};

app.models = {};

app.models.Session = function(data) {
    this.id = m.prop(data.id);
    this.email = m.prop(data.email);
    this.password = m.prop(data.password);
    this.token = m.prop(data.token);
};

app.models.Session.validator = new m.validator({
        // Check model name property
        email: function (email) {
            console.log(email);
            if (!email) {
                return "Email is required."
            }
            if (!app.tools.validateEmail(email)) {
                return 'Invalid e-mail address.';
            }
            return false;
        },
        password: function (password) {
            if (!password) {
                return "Password is required.";
            }
        }
});

app.widgets = {};

// Bootstrap element widgets
app.widgets.bootstrap = {
    form: function(elements, opts) {
        opts = opts || {};
        return [m('form', opts, elements)];
    },
    formGroup: function(el_type, name, label, opts, hasErrors) {
    opts = opts || {};
    hasErrors = hasErrors || false;
    var defaults = {
        name: name,
        id: name,
        class: 'form-control'
    };
    var cls = hasErrors ? '.form-group .has-error' : '.form-group';
    opts = $.extend(defaults, opts);
        return [m(cls, [m('label', {'for': name}, label), m(el_type, opts)])];
    },
    button: function(caption, opts) {
        opts = opts || {};
        var defaults = {
            class: 'btn btn-default'
        };
        opts = $.extend(defaults, opts);
        return [m('button', opts, caption)];
    }
};

app.models.Session.getState = function() {
    //TODO: add cookies check first
    return m.request({method: "GET", url: "/api/sessions/", type: app.models.Session});
};

app.models.Session.isLoggedIn = function() {
    var state = this.getState();
    console.log(this.id);
    if (this.id) {
        return true;
    } else {
        return false;
    }
};

// login module
app.loginModule = {};

app.loginModule.controller = function(){
    var ctrl = this;
    ctrl.loginData = new app.models.Session([]);
    ctrl.validator = app.models.Session.validator.validate(ctrl.loginData);
    ctrl.signIn = function(e) {
        var that = this;
        var $that = $(that);
        e.preventDefault();
        console.log(ctrl.validator.hasErrors());
        if (!ctrl.validator.hasErrors()) {
            $that.button('loading');
        $that.prop('disabled', true);
        m.request({method: "POST", url: "/api/sessions/", data: ctrl.loginData, type: app.models.Session}).then(
            // success
            function(response) {
                console.log(response);
                $that.button('reset');
                $that.prop('disabled', false);
            },
            // error
            function(response) {
                console.log(response);
                $that.button('reset');
                $that.prop('disabled', false);
            }
        );
        }
    }
};
app.loginModule.view = function(ctrl){
    return m('.row', [ m('.col-md-8', [m('h3', 'Login'), app.widgets.bootstrap.form([
        app.widgets.bootstrap.formGroup('input', 'email', 'Email address', {
            placeholder: 'Enter your email here',
            value: ctrl.loginData.email(),
            onchange: m.withAttr("value", ctrl.loginData.email)
        }, ctrl.validator.hasError('email')),
        app.widgets.bootstrap.formGroup('input', 'pass', 'Password', {
            type: 'password',
            placeholder: 'Your password here',
            value: ctrl.loginData.password(),
            onchange: m.withAttr("value", ctrl.loginData.password)
        }, ctrl.validator.hasError('password')),
        app.widgets.bootstrap.button('Submit', {
            onclick: ctrl.signIn,
            'data-loading-text': "<i class='fa fa-cog fa-spin'></i> Loading..."
        })
        ], {action: '#', id: 'loginHandle'}
    )]) ]);

};

app.homeModule = {};
app.homeModule.controller = function(){
    if (!app.models.Session.isLoggedIn()) {
        console.log('redirecting to login');
        m.route("/login");
    }
};
app.homeModule.view = function(ctrl) {
    console.log('in home view');

    return m("div","<h1>HOME</h1>");
};

app.aboutModule = {};
app.aboutModule.controller = function() {};
app.aboutModule.view = function(ctrl) {
    return m('.row', [ m('.col-md-8', [m('h3', 'About page'), m('p', 'Hello, world!')]) ]);
};

m.route.mode = "hash";
m.route( $('#application').get(0), '/library', {
    '/login' : app.loginModule,
    '/library'  : app.homeModule,
    '/about': app.aboutModule
} );