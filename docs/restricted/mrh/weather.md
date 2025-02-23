<script>
document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("nav").style.display = "none";  // Hide the navigation
    document.querySelector(".md-header").style.display = "none"; // Hide the header
    document.querySelectorAll("nav, h1").forEach(el => el.style.display = "none");
});
</script>
<div id="image-container" style="width:100%; text-align:center;">
    <img id="radar-image" src="" style="max-width:100%; height:auto;" alt="Loading radar images...">
</div>
<script>
    function pad(num, size) {
        return ('0000' + num).slice(-size);
    }

    function generateImageUrls() {
        const baseUrl = "https://radar.ozforecast.com.au/composites/Australia/";
        let images = [];
        const now = new Date();
        now.setUTCMinutes(now.getUTCMinutes() - (now.getUTCMinutes() % 10));  // Round to nearest 10 minutes
        now.setUTCSeconds(0);

        for (let i = 0; i < 15; i++) {
            let dateString = now.getUTCFullYear() +
                             pad(now.getUTCMonth() + 1, 2) +
                             pad(now.getUTCDate(), 2) + "-" +
                             pad(now.getUTCHours(), 2) +
                             pad(now.getUTCMinutes(), 2);
            images.unshift(`${baseUrl}Australia-${dateString}_970.jpg`);
            now.setUTCMinutes(now.getUTCMinutes() - 10);  // Move back 10 minutes
        }
        return images;
    }

    function cycleImages(imageUrls) {
        let index = 0;
        const imgElement = document.getElementById("radar-image");

        function updateImage() {
            imgElement.src = imageUrls[index];
            index = (index + 1) % imageUrls.length;
            if (index === 0) {
                setTimeout(updateImage, 3000); // Pause for 3 seconds after a full cycle
            } else {
                setTimeout(updateImage, 500); // Show each image for 0.5s
            }
        }

        updateImage();
    }

    document.addEventListener("DOMContentLoaded", function() {
        const imageUrls = generateImageUrls();
        cycleImages(imageUrls);
    });

</script>
