var initCounter = (function(){
	document.querySelector("body").addEventListener("click",function(e){
		if(e.target.classList.contains('tt-btn-minus')){
			var objInput = e.target.parentNode.querySelector('.tt-counter__input'),
				getValue = parseInt(objInput.value);
			setValue('minus', objInput, getValue);
		};
		if(e.target.classList.contains('tt-btn-plus')){
			var objInput = e.target.parentNode.querySelector('.tt-counter__input'),
				getValue = parseInt(objInput.value);
			setValue('plus', objInput, getValue);
		};
	});
	function setValue(action,objInput,getValue){
		if(action === "minus"){
			var newValue = getValue - 1;
			objInput.value = newValue;
		};
		if(action === "plus"){
			var newValue =  getValue + 1;
			objInput.value = newValue;
		};
	};
}());