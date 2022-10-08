class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class linkedList{
    constructor(){
        this.root = null;
    }

    push(val) {
        let new_node = new Node(val);
        new_node.next = this.root;
        this.root = new_node;
    }

    add(val) {
        let new_node = new Node(val);
        let last = this.root;
        while (last.next != null) {
            last = last.next;
        }
        last.next = new_node;
        return 0;
    }

    printList() {
        let res = [];
        let cur = this.root;
        while (cur) {
            res.push(cur.val);
            cur = cur.next;
        }
        console.log(res.join(" "));
        return 0;
    }
}

let mylist = new linkedList();
mylist.push(5);
mylist.push(4);
mylist.push(3);
mylist.push(2);
mylist.push(1);
mylist.add(6);
mylist.printList();