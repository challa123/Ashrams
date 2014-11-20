/**
 * jQuery for home.html
 */
$(document).ready(function() {
});
$(window).load(function(){
    childCountAnimate(100);
    ashramCountAnimate(10);
});
function childCountAnimate(count) {
     $('#children-count')
            .prop('number', 000)
            .animateNumber(
            {
                number: count
            },
            2000
        );
}
function ashramCountAnimate(count){
     $('#ashram-count')
            .prop('number', 00)
            .animateNumber(
            {
                number: count
            },
            2000
        );
}
