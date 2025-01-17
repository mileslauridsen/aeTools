Expression_path = "/Users/aitor/.nuke/Expression"
nuke.pluginAddPath(Expression_path)

# AITOR ECHEVESTE TOOLS
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Aitor Echeveste", icon="AitorEchevesteNukeLogo.png")
m.addCommand("aeBrokenEdges", "nuke.createNode(\"aeBrokenEdges\")", icon="BrokenEdges_icon.png")
m.addCommand("aeAnamorphic", "nuke.createNode(\"aeAnamorphic\")", icon="aeAnamorphic_icon.png")
m.addCommand("aeFiller", "nuke.createNode(\"aeFiller\")", icon="aeFiller_icon.png")
m.addCommand("aeBrokenShapes", "nuke.createNode(\"aeBrokenShapes\")", icon="BrokenShapes_icon.png")
m.addCommand("aePowerPin", "nuke.createNode(\"aePowerPin\")", icon="aePowerPin_icon.png")
#m.addCommand("aeSnapShot", "nuke.createNode(\"aeSnapShot\")")
m.addCommand("aeTransform", "nuke.createNode(\"aeTransform\")", icon="aeTransform_icon.png")
m.addCommand("aeRelight2D", "nuke.createNode(\"aeRelight2D\")", icon="aeReLight2D_icon.png")
m.addCommand("aeRefracTHOR", "nuke.createNode(\"aeRefracTHOR\")", icon="aeRefracTHOR_icon.png")
m.addCommand("aeMotionBlur", "nuke.createNode(\"aeMotionBlur\")", icon="aeMotionBlur_icon.png")


if nuke.NUKE_VERSION_MAJOR < 12:
	m.addCommand("iSTMap", "nuke.createNode(\"iSTMap11\")", icon="iSTMap_icon.png")
else:
	m.addCommand("iSTMap", "nuke.createNode(\"iSTMap\")", icon="iSTMap_icon.png")