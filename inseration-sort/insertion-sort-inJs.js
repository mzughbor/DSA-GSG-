//JavaScript Implementation Here’s how you can implement Insertion Sort in JavaScript: 
function insertionSort(arr) {
    // Start from the second element
    for (let i = 1; i < arr.length; i++) {
        let current = arr[i]; // Current element to be inserted
        let j = i - 1;

        // Shift elements of the sorted portion to the right
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j]; // Shift element to the right
            j--; // Move to the next element on the left 
        }

        // Insert the current element at the correct position 
        arr[j + 1] = current;
    }
    return arr;
}

// Example usage
const numbers = [7, 3, 5, 2, 6];
// i = 2 >> j = 1 >> do swap if the confistion is true then -j by one, j=0 , i=2
// so each time the for loop increase by one i , the while loope exten the comparing cyrcle by one...
console.log("Sorted Array:", insertionSort(numbers)); // Output: [2, 3, 5, 6, 7]


