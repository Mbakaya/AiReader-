import demo_lib

#accept user to input

demo_lib.get_user_input()

#return dependency tree
dep_tree = demo_lib.create_dependency_tree()

#retrieve root word and dependent object
root = demo_lib.get_root_word(dep_tree)

#retireve synonym for root word
synonym = demo_lib.get_synonym(root)

#display
print 'intent is | ' +synonym + ''+ obj
