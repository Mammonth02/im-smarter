var toggleAsideListing = (function(){
	var objAside = document.getElementById("js-toggle__aside"),
		objToggleBtn = document.getElementById("js-toggle__btn"),
		$body = document.body,
		$objLockOffsetRight = document.querySelector("#js-init-sticky");

	if(objAside && objToggleBtn){
		var modalOverlay = document.getElementById("js-toggle__btn");
		if(modalOverlay){
			$body.insertAdjacentHTML('beforeend', '<div id="modal__overlay"></div>');
		}
		objToggleBtn.addEventListener("click", function(e){
			e.preventDefault();
			var target = event.target,
				withScroll = window.innerWidth - document.documentElement.clientWidth;

			showPopup(target, withScroll);
		});
	};
	function showPopup(target, withScroll){
		$body.classList.add('show-popup')
		target.classList.add('active');
		objAside.classList.add('show-popup');
		new PerfectScrollbar(objAside);
		hangHandlerClose();
		lockOffsetTop();
		lockOffsetRight(withScroll);
		disableScroll();
	};
	function lockOffsetTop(){
		var valueScroll = $body.scrollTop || document.documentElement.scrollTop;
		$body.style.top = valueScroll + 'px';
	}
	function lockOffsetRight(withScroll){
		$body.style.paddingRight = withScroll + 'px';
		if($objLockOffsetRight.classList.contains('sticky-header')){
			$objLockOffsetRight.style.paddingRight = withScroll + 'px';
		}
	}
	function closePopup(){
		$body.classList.remove('show-popup');
		$body.removeAttribute("style");
		$objLockOffsetRight.removeAttribute("style");
		objAside.classList.remove('show-popup');
		objToggleBtn.classList.remove('active');
		new PerfectScrollbar(objAside).destroy();
		enableScroll();
	};
	function hangHandlerClose(){
		objAsideClose = document.getElementById("js-aside-close");
		objAsideClose.addEventListener("click", function(e){
			closePopup();
		});
	};
	document.addEventListener('click', function(event) {
		var e=document.getElementById('modal__overlay');
		if (e.contains(event.target)){
			closePopup();
		};
	});
	function preventDefault(e){
		e.preventDefault();
	};
	function disableScroll(){
		window.addEventListener('touchmove', preventDefault, { passive: false });
	};
	function enableScroll(){
		window.removeEventListener('touchmove', preventDefault,  { passive: false });
	};
}());
