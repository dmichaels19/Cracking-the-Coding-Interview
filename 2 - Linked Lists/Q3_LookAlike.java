public class LookAlike {
    public static void main(String[] args) {
        Node head = new Node(1);
        head.add(2);
        head.add(3);
        head.add(4);
        head.add(5);
        head.add(6);
        Node c = head.next.next;
        System.out.println(c.data);
        c.data = c.next.data;
        c.next = c.next.next;
        System.out.println(head.printList());
    }
}