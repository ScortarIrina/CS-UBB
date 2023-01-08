; Determine the list of nodes accesed in postorder in a tree of type (1).


; parse_left(l1 l2 ... ln, no_nodes, no_edges) = { nil, if n = 0
;                                              = { nil, if no_nodes = 1 + no_edges
;                                              = { {l1} U {l2} U parse_left(l3 ... ln, no_nodes + 1, l2 + no_edges), otherwise
; function to parse the left subtree and count the number of nodes and vertices
(defun parse_left (l no_nodes no_edges)
  (cond
    ((null l) nil)
    ((= no_nodes ( + 1 no_edges)) nil)
    (t (cons (car l) (cons (cadr l) (parse_left (cddr l) (+ 1 no_nodes) (+ (cadr l) no_edges)))))
  )
)


; parse_right(l1 l2 ... ln, no_nodes, no_edges) = { nil, if n = 0
;                                               = { l1 l2 ... ln, if no_nodes = 1 + no_edges
;                                               = { parse_right(l3 ... ln, no_nodes + 1, no_edges + l2), otherwise
; f; function to parse the right subtree and count the number of nodes and vertices
(defun parse_right (l no_nodes no_edges)
  (cond
    ((null l) nil)
    ((= no_nodes (+ 1 no_edges)) l)
    (t (parse_right (cddr l) (+ 1 no_nodes) (+ (cadr l) no_edges)))
  )
)


; left(l1 l2 ... ln) = { parse_left(l3 ... ln, 0, 0)
; aux function which calls parse_left
(defun left(l)
  (parse_left (cddr l) 0 0)
)


; right(l1 l2 ... ln) = { parse_right(l3 ... ln, 0, 0)
; aux function which calls parse_right
(defun right(l)
  (parse_right (cddr l) 0 0)
)


; postorder(l1 l2 ... ln) = { nil , if n = 0
;                         = { postorder(left(l1 l2 ... ln)) U postorder(right(l1 l2 ... ln) U l1 , otherwise
; function which builds the postorder traversal of the tree
(defun postorder (l)
  (cond
    ((null l) nil)
    (t (my_append (postorder(left l)) (my_append (postorder(right l)) (list (car l)))))
  )
)

; my_append(l1 l2 ... ln, p1 p2 ... pm) = { p1 p2 ... pm, if n = 0
;                                       = { {l1} U my_append(l2 ... ln, p1 p2 ... pm), otherwise
(defun my_append(l p)
  (cond
    ((null l) p)
    (t (cons (car l) (my_append (cdr l) p)))
  )
) 


(defun test_postorder ()
    (assert
	    (and
	        (equal '(B D E C A) (postorder '(A 2 B 0 C 2 D 0 E 0)))
	        (equal '(F B E D A) (postorder '(A 2 B 1 F 0 D 1 E 0)))
          (equal '(F B E G D A) (postorder '(A 2 B 1 F 0 D 2 E 0 G 0)))
          (equal '(E F D B G K I J H C A) (postorder '(A 2 B 1 D 2 E 0 F 0 C 2 G 0 H 2 I 1 K 0 J 0)))
	    )
    )
)


;   FIRST TEST             SECOND TEST            THIRD TEST
;
;       A                       A                     A
;      / \                     / \                   / \
;     B   C                   B   D                 B   D
;        / \                 /   /                 /   / \
;       D   E               F   E                 F   E   G




; (compile-file "/Users/irinascortar/Desktop/VSCode_projects/LISP/l1b/14.lisp")
; (load "/Users/irinascortar/Desktop/VSCode_projects/LISP/l1b/14.lisp")