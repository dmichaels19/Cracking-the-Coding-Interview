import java.util.HashSet;
public class RemoveDups {
    public static void main (String[] args) {
	int[] nums = {7,7,7,6,6,5,6,7,5,4,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7,7,7,7,6,6,5,6,7,5,6,5,7};
	Node head = new Node(nums[0]);
	for (int i = 1; i < nums.length; i++) {
	    head.add(nums[i]);
	}
	long begin = System.nanoTime();
	//System.out.println(head.printList());
	removeDups(head);
	begin = System.nanoTime() - begin;
	System.out.println(head.printList() + begin);
    }
    public static void removeDups (Node head) {
	Node a = head;
	Node b = a;
	while (a.next != null) {
	    while (b.next != null) {
		if (b.next.data==a.data) {
		    b.next = b.next.next;
		} else {
		    b = b.next;
		}
	    }
	    a = a.next;
	    b = a;
	}
    }
    public static void removeDupsHash (Node head) {
	HashSet<Integer> set = new HashSet<Integer>();
	set.add(head.data);
	Node n = head;
	while (n.next != null) {
	    if (set.contains(n.next.data)) {
		n.next = n.next.next;
	    } else {
		set.add(n.next.data);
		n = n.next;
	    }
	}
		
    }
}