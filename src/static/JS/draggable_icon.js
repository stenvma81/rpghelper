function makeIconDraggable(draggableElement, boundaryElement) {
    let currentMouseX = 0, currentMouseY = 0;

    draggableElement.onmousedown = function(event) {
        event.preventDefault();
        currentMouseX = event.clientX;
        currentMouseY = event.clientY;
        document.onmouseup = endDrag;
        document.onmousemove = performDrag;
    };

    function performDrag(event) {
        event.preventDefault();

        const deltaX = currentMouseX - event.clientX;
        const deltaY = currentMouseY - event.clientY;
        currentMouseX = event.clientX;
        currentMouseY = event.clientY;

        const newLeftPercent = ((draggableElement.offsetLeft - deltaX) / boundaryElement.offsetWidth) * 100;
        const newTopPercent = ((draggableElement.offsetTop - deltaY) / boundaryElement.offsetHeight) * 100;

        draggableElement.style.left = `${newLeftPercent}%`;
        draggableElement.style.top = `${newTopPercent}%`;
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