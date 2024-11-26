function loadContent(page) {
  const mainContent = document.getElementById('main-content');

  // Check if the main content element exists
  if (!mainContent) {
    console.error('Error: Element with id "main-content" not found.');
    return;
  }

  // Log the page being fetched for debugging purposes
  console.log(`Fetching content from: pages/${page}`);

  // Fetch the requested page
  fetch(`pages/${page}`)
    .then((response) => {
      if (!response.ok) {
        // Throw a detailed error for debugging if the fetch fails
        throw new Error(`Failed to load page "${page}": ${response.status} - ${response.statusText}`);
      }
      return response.text();
    })
    .then((html) => {
      // Update the main content with the fetched HTML
      mainContent.innerHTML = html;
    })
    .catch((error) => {
      // Log the error to the console for debugging
      console.error('Error loading content:', error);

      // Display a user-friendly error message in the main content area
      mainContent.innerHTML = `
        <div class="error-message" style="color: red; font-weight: bold; padding: 10px; border: 1px solid red; background: #ffe6e6;">
          <p>Unable to load content. Please try again later.</p>
          <p>Error: ${error.message}</p>
        </div>
      `;
    });
}

