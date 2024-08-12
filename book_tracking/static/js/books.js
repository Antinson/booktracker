// Function to fetch books from the server
async function fetchBooks(page = 1, perPage = 10) {
    try {
      // Construct the URL with query parameters
      const url = new URL('/getbooks', window.location.origin);
      url.searchParams.append('page', page);
      url.searchParams.append('per_page', perPage);
  
      // Perform the fetch request
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          // Include other headers if needed (e.g., Authorization)
        },
      });
  
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`An error occurred: ${response.status} ${response.statusText}`);
      }
  
      // Parse the JSON response
      const data = await response.json();
  
      // Process the data as needed
      console.log('Books:', data.books);
      console.log('Total Pages:', data.pages);
      console.log('Total Books:', data.total);
      console.log('Has Next Page:', data.has_next);
      console.log('Has Previous Page:', data.has_prev);
  
      // Load books into the carousel
      loadBooks(data.books);
  
      // Return the data for further processing if needed
      return data;
    } catch (error) {
      // Handle errors
      console.error('Error fetching books:', error);
    }
  }
  
  // Function to add a new book to the server
  async function addBook(bookData) {
    try {
      // Construct the URL for adding a book
      const url = new URL('/addbook', window.location.origin);
  
      // Perform the fetch request
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Include other headers if needed (e.g., Authorization)
        },
        body: JSON.stringify(bookData), // Convert the book data to a JSON string
      });
  
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`An error occurred: ${response.status} ${response.statusText}`);
      }
  
      // Parse the JSON response
      const data = await response.json();
  
      // Process the data as needed
      console.log('Response:', data.message);
      console.log('Added Book Title:', data.book);
  
      // Fetch updated list of books after adding a new one
      fetchBooks(1, 10);
  
      // Return the data for further processing if needed
      return data;
    } catch (error) {
      // Handle errors
      console.error('Error adding book:', error);
    }
  }
  
  // Function to dynamically load books into the carousel
  function loadBooks(books) {
    const bookEntries = document.getElementById('books-entries');
    bookEntries.innerHTML = ''; // Clear existing entries
  
    books.forEach(book => {
      const bookCard = document.createElement('div');
      bookCard.className = 'book-card';
      bookCard.innerHTML = `
        <img src="${book.book_cover || '../static/images/default_cover.jpg'}" alt="${book.title}">
        <h3>${book.title}</h3>
      `;
      bookEntries.appendChild(bookCard);
    });
  }
  
  // Function to scroll the carousel
  function scrollCarousel(amount) {
    const bookEntries = document.getElementById('books-entries');
    bookEntries.scrollBy({ left: amount, behavior: 'smooth' });
  }
  
  // Example usage:
  const newBook = {
    title: 'Introduction to Machine Learning',
    pages: 350,
    semester: 'Fall 2024',
    class_name: 'ML101',
    book_cover: 'https://example.com/covers/ml101.jpg',
    subject: 'Computer Science',
    pages_read: 0 // Optional, defaults to 0 if not provided
  };
  
  // Load books when the page is ready
  document.addEventListener('DOMContentLoaded', () => {
    addBook(newBook); // Add the new book to the server
    fetchBooks(1, 10); // Fetch the first page with 10 books per page
  });
  