document.addEventListener('DOMContentLoaded', function () {
	const form = document.getElementById('botForm')
	form.addEventListener('submit', function (event) {
		const nameInput = document.getElementById('id_name')
		const descriptionInput = document.getElementById('id_description')

		if (!nameInput.value.trim()) {
			alert('Please enter a bot name.')
			event.preventDefault()
			return
		}

		if (!descriptionInput.value.trim()) {
			alert('Please enter a description.')
			event.preventDefault()
			return
		}
	})
})
