MarginaliaApp.controller('BookCreateCtrl', function ($scope, $location, Book) {
    $scope.submit = function (isValid, book) {
        $scope.submitted = true;
        $scope.bookCreateForm.$setDirty();

        if (!isValid) {
            return;
        }

        Book.create(book).then(function (response) {
            $location.path('/');
        });
    };
});