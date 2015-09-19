$(document).ready(function() {
	$('#seeAll').on('click', function() {
		$('.o_2').toggleClass('c_2')
		$('.o_3').toggleClass('c_3')

		if ($('#seeAllText').text() == 'See all >>')
			$('#seeAllText').text('<< Not done only')
		else
			$('#seeAllText').text('See all >>')
	})
})