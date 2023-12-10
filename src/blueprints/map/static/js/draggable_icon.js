function makeIconDraggable(draggableElement, boundaryElement) {
    let isDragging = false;
    let startX = 0, startY = 0;

    draggableElement.addEventListener('mousedown', startDrag);

    function startDrag(event) {
        event.preventDefault();
        isDragging = true;

        startX = event.clientX;
        startY = event.clientY;

        document.addEventListener('mousemove', performDrag);
        document.addEventListener('mouseup', endDrag);
    }

    function performDrag(event) {
        if (!isDragging) return;
    
        let deltaX = startX - event.clientX;
        let deltaY = startY - event.clientY;

        let newLeft = draggableElement.offsetLeft - deltaX;
        let newTop = draggableElement.offsetTop - deltaY;
    
        let minLeft = 0;
        let maxLeft = boundaryElement.offsetWidth - draggableElement.offsetWidth;
        let minTop = 0;
        let maxTop = boundaryElement.offsetHeight - draggableElement.offsetHeight;
    
        newLeft = Math.max(minLeft, Math.min(newLeft, maxLeft));
        newTop = Math.max(minTop, Math.min(newTop, maxTop));
    
        const newLeftPercent = (newLeft / boundaryElement.offsetWidth) * 100;
        const newTopPercent = (newTop / boundaryElement.offsetHeight) * 100;
    
        draggableElement.style.left = `${newLeftPercent}%`;
        draggableElement.style.top = `${newTopPercent}%`;
    
        startX = event.clientX;
        startY = event.clientY;
    }

    function endDrag() {
        if (!isDragging) return;

        document.removeEventListener('mousemove', performDrag);
        document.removeEventListener('mouseup', endDrag);

        isDragging = false;
    }
}

window.addEventListener('load', function() {
    const characterElement = document.getElementById('character');
    const mapContainerElement = document.getElementById('mapContainer');
    makeIconDraggable(characterElement, mapContainerElement);
});

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
