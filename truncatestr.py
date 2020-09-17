def truncatestr(str, num):
    
    if len(str) > num:
        print(str[:num] + "...")

truncatestr("A-tisket a-tasket A green and yellow basket", 8)
truncatestr("Peter Piper picked a peck of pickled peppers", 11)