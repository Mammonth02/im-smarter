var galleryItem = (function(){
	var galleryView = document.querySelector("#gallery-item__large img"),
		galleryThumbnail = document.getElementById("gallery-item__thumbnail");

	if(galleryView && galleryThumbnail){
		if(document.body.classList.contains('touch-device')){
			var objEvents = 'touchstart';
		} else {
			var objEvents = 'click';
		};
		Array.prototype.slice.call(galleryThumbnail.querySelectorAll('div[data-image]')).forEach(function(el) {
			el.addEventListener(objEvents, changingImage);
		});
	};
	function changingImage(el){
		Array.prototype.slice.call(galleryThumbnail.querySelectorAll('div[data-image]')).forEach(function(item){
			if(item.classList.contains('active')){
				item.classList.remove('active');
			}
		});
		galleryView.src = el.currentTarget.dataset.image;
		el.currentTarget.classList.add('active');
	};
}());
