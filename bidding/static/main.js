$(function() {
	$.ajaxSetup({
        headers: { "X-CSRFToken": Cookies.get("csrftoken") }
    });

	$('#search').on('submit', function(e) {
		e.preventDefault();
		var search = this.search.value;
		$.ajax({
			method: "GET",
			url: "/search",
			data: {
				'search': search
			},
			success: function(data) {
				console.log(data);
				$('#results').html(data);
			},
			error: function() {
				$('#results').prepend("<div class='alert alert-danger'>An error occurred.</div>");
			}
		});
	});
});