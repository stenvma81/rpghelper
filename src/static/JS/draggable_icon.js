function makeIconDraggable(draggableElement, boundaryElement) {
    let offsetX = 0, offsetY = 0, currentMouseX = 0, currentMouseY = 0;

    draggableElement.onmousedown = initiateDrag;

    function initiateDrag(event) {
        event.preventDefault();
        currentMouseX = event.clientX;
        currentMouseY = event.clientY;

        document.onmouseup = endDrag;
        document.onmousemove = performDrag;
    }

    function performDrag(event) {
        event.preventDefault();

        offsetX = currentMouseX - event.clientX;
        offsetY = currentMouseY - event.clientY;
        currentMouseX = event.clientX;
        currentMouseY = event.clientY;

        const newTop = calculateNewPosition(draggableElement.offsetTop - offsetY, 'top');
        const newLeft = calculateNewPosition(draggableElement.offsetLeft - offsetX, 'left');

        draggableElement.style.top = newTop + 'px';
        draggableElement.style.left = newLeft + 'px';
    }

    function calculateNewPosition(newPosition, axis) {
        const boundaryDimension = axis === 'top' ? boundaryElement.offsetHeight : boundaryElement.offsetWidth;
        const draggableDimension = axis === 'top' ? draggableElement.offsetHeight : draggableElement.offsetWidth;

        if (newPosition < 0) {
            return 0;
        }

        if (newPosition + draggableDimension > boundaryDimension) {
            return boundaryDimension - draggableDimension;
        }

        return newPosition;
    }

    function endDrag() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

window.onload = function() {
    const characterElement = document.getElementById('character');
    const mapContainerElement = document.getElementById('mapContainer');
    makeIconDraggable(characterElement, mapContainerElement);
};
