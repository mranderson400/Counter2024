document.addEventListener('DOMContentLoaded', function() {
    var changeableImage = document.getElementById('changeable-image');

  
    var originalImage = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc59gKtgRQj12yP5tWFpwYpJCZ1J0QfxzNwA&usqp=CAU";
    var hoverImage = "https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-walking-dead/0/0a/Daryl-dixon-picture.jpg";

    changeableImage.addEventListener('mouseover', function() {
        changeableImage.src = hoverImage;
    });

    changeableImage.addEventListener('mouseout', function() {
        changeableImage.src = originalImage;
    });
});