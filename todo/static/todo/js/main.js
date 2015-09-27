$(document).ready(function() {
	$('#seeAll').on('click', function() {
		$('.o_2').toggleClass('c_2')
		$('.o_3').toggleClass('c_3')

		if ($(this).attr('value') == 'See all >>')
			$('#seeAll').val('<< Not done only')
		else
			$('#seeAll').val('See all >>')
	})
})