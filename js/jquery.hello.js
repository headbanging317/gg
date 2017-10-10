
(function($){
	// hello 는 jquery 추가 기능의 함수 명이다. 
	$.fn.hello=function(){
		// this 는 선택된 jquery object 를 가리킨다 
		this.text("hello");

		return this; // chain 형태로 동작 가능하게 
	};
})(jQuery);