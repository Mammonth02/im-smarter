var initPriceSlider = (function () {
	var snapSlider = document.getElementById('slider-snap');
	if (snapSlider){
		var objLower = document.getElementById('slider-snap-value-lower');
		var objUpper = document.getElementById('slider-snap-value-upper');
		noUiSlider.create(snapSlider, {
		  start: [ 0, 2000 ],

		  range: {
			'min': [0],
			'max': 2000
		  }
		});
		var snapValues = [
		  document.getElementById('slider-snap-value-lower'),
		  document.getElementById('slider-snap-value-upper')
		];
		snapSlider.noUiSlider.on('update', function( values, handle, unencoded  ) {
		  snapValues[handle].innerHTML = values[handle];
		});
		snapSlider.noUiSlider.on('update', function () {
			rounding();
		});
	};
	function rounding(){
		objLower.innerText =  parseInt(objLower.innerHTML);
		objUpper.innerText = parseInt(objUpper.innerHTML);
	}
}());
