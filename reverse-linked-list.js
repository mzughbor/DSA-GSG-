/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    let current = head; // don't toutch the real head
    let previous = null;
    while (current != null) {
        let next = current.next;
        current.next = previous; // reverse linking
        previous = current;
        current = next;

    }
    return previous;
};