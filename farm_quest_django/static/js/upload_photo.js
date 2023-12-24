
        function openCamera() {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => {
                    const videoElement = document.createElement('video');
                    videoElement.srcObject = stream;
                    videoElement.play();

                    const canvasElement = document.createElement('canvas');
                    canvasElement.width = videoElement.width;
                    canvasElement.height = videoElement.height;
                    const canvasContext = canvasElement.getContext('2d');

                    videoElement.addEventListener('loadedmetadata', () => {
                        canvasContext.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
                        const imageDataUrl = canvasElement.toDataURL('image/jpeg');

                        const photoInput = document.getElementById('photoInput');
                        photoInput.value = imageDataUrl;

                        // Stop capturing video to release the camera
                        stream.getTracks().forEach(track => track.stop());
                    });
                })
                .catch(error => {
                    console.error('Error accessing camera:', error);
                });
        }
