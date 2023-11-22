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

document.getElementById('characterSelect').addEventListener('change', function() {
    const selectedOption = this.options[this.selectedIndex];
    const characterName = selectedOption.getAttribute('data-name');
    const characterHealth = selectedOption.getAttribute('data-health');
    const characterArmorClass = selectedOption.getAttribute('data-armorclass');

    updatePlayerIcon(characterName, characterHealth, characterArmorClass);
});

function updatePlayerIcon(characterName, characterHealth, characterArmorClass) {
    const playerIcon = document.getElementById('playerIcon');

    document.getElementById('nameTag').textContent = characterName;
    document.getElementById('healthBar1').textContent = characterHealth;
    document.getElementById('healthBar2').textContent = characterArmorClass;
}