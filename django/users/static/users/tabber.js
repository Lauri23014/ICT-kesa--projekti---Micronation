function openTab(evt, tabName) {
	// Declare all variables
	var i, tabContent, tabButtons;

	// Get all elements with class="tabContent" and hide them
	tabContent = document.getElementsByClassName("tabber-content");
	for (i = 0; i < tabContent.length; i++) {
		tabContent[i].style.display = "none";
	}

	// Get all elements with class="tabButtons" and remove the class "active"
	tabButtons = document.getElementsByClassName("tab-buttons");
	for (i = 0; i < tabButtons.length; i++) {
		tabButtons[i].className = tabButtons[i].className.replace(" active", "");
	}

	// Show the current tab, and add an "active" class to the button that opened the tab
	document.getElementById(tabName).style.display = "block";
	evt.currentTarget.className += " active";
} 