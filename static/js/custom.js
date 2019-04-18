function enterFullScreen(mediaType) {
	var elem = $(mediaType).get(0);
	if (elem.requestFullscreen) {
		elem.requestFullscreen();
	} else if (elem.mozRequestFullScreen) {
		elem.mozRequestFullScreen();
	} else if (elem.webkitRequestFullscreen) {
		elem.webkitRequestFullscreen();
	} else if (elem.msRequestFullscreen) { 
		elem.msRequestFullscreen();
	} else if (elem.oRequestFullscreen) {
		elem.oRequestFullscreen();
	}
	
	return elem;
}

function exitFullScreen(mediaType) {
	$(mediaType).bind('webkitfullscreenchange mozfullscreenchange msfullscreenchange ofullscreenchange fullscreenchange', function(e) {
		var isFullScreen = document.fullScreen || document.mozFullScreen || document.webkitIsFullScreen || document.msFullscreen || document.oFullScreen;
		if (!isFullScreen) {
			$('#media-header').empty();
			$('#media-content').empty();
			$('#media-header').text('Choose content');
			$('#media-content').html('<p>Content will be displayed here.</p>');
		}
	});
}

$(document).ready(function() {
	$('.navbar-nav>li>a').mouseenter(function() {
		$(this).find('path').attr('fill', '#333333');
	});
	$('.navbar-nav>li>a').mouseleave(function() {
		$(this).find('path').attr('fill', '#777777')
	});
	var remainingHeight = ($(window).height() - $('#topnav').height() - $('#topnav').height() - $('#content').height()).toFixed();
	if (remainingHeight > 0)
	{
		$('#blank').css('height', remainingHeight + 'px');
	}
	if ($('#topnav').hasClass('navbar-fixed-top')) {
		$('#content').css('margin-top', $('#topnav').height() * 1.4);
	}
	var ctl = [];
	var mtl = [];
	$('#material-list li').each(function() {
		if($(this).hasClass('list-group-item-success')) {
			var ctxt = $(this).text();
			if(ctl.includes(ctxt)) {
				$(this).remove();
			} else {
				ctl.push(ctxt);
			}
		}
		if($(this).hasClass('list-group-item-info')) {
			var mtxt = $(this).text();
			if(mtl.includes(mtxt)) {
				$(this).remove();
			} else {
				mtl.push(mtxt);
			}
		}
	});
	var materialListOverflowHeight = ($(window).height() - $('#media-header').height() - $('#topnav').height() - $('#topnav').height()).toFixed();
	if ($('#material-list').height().toFixed() > materialListOverflowHeight) {
		$('#material-list').height(materialListOverflowHeight);
		$('#material-list').addClass('vertical-scroll');
	} else {
		$('#material-list').removeClass('vertical-scroll');
	}
	$('#material-list li.btn-default').click(function() {
		$('#media-header').empty();
		$('#media-content').empty();
		$('#media-header').text($(this).attr('data-label'));
		if($(this).attr('data-type') == 'VID') {
			$('#media-content').append('<video src="' + $(this).attr('data-url') + '" controls controlsList="nodownload">Your browser does not support the video tag.</video>');
		}
		if($(this).attr('data-type') == 'GFORM') {
			$('#media-content').append('<embed src="' + $(this).attr('data-url') + '" target="_blank">');
		}
		var materialHeight = ($(window).height() - $('#media-header').height() - $('#topnav').height() - $('#topnav').height() - $('#topnav').height() - $('#topnav').height()).toFixed();
		var materialWidth = materialHeight * 16 / 9;
		if ($(window).width() > 799) {
			$('video, embed').attr('width', materialWidth);
			$('video, embed').attr('height', materialHeight);
		} else {
			if($(this).attr('data-type') == 'VID') {
				enterFullScreen('video').play();
				exitFullScreen('video');
			}
			if($(this).attr('data-type') == 'GFORM') {
				enterFullScreen('embed');
				$('embed').height('100vh');
				$('embed').width('100vw');
				$('embed').css('padding-top', '25vh');
				exitFullScreen('embed');
			}
		}
	});
});
