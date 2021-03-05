def encryption(): # function to encrypt the plain text.
          Plaintext = input("enter the plain text ") # ask the user to input plaintext
          Key = input("give the value of the key ") # ask the user to input the value of the key
          
          result = "" # to store the value of result
          matrix = [["" for x in range(len(Plaintext))]for y in range(int(Key))] # a list of empty strings with rows equal to the value of key(main list) and columns equal to the length of the plain text(dimensions of the inner list).

          increment = 1 # initialize the value of increment to 1
          row = 0 # set the row value to 0
          col = 0 # set the column value to 0

          for c in Plaintext: # to read each character in the plain text.
                    if row + increment < 0 or row + increment >= len(matrix): # checking if we are going out of the boundaries.
                              increment = increment * -1 # if yes, then getting it back into the matrix. Eg: 1 -> -1, -1 -> 1.
                    matrix[row][col] = c # if the 'if' condition is false, we place the character in the matrix.

                    row += increment # increment the row.
                    col += 1 # increment the column.
          for list in matrix: # for each list in the matrix.
                    result += "".join(list) # we are picking each character in the list of lists and concatenating to form a ciphertext.
          return result # returning the result to the encryption function.

def decryption(): #function to decrypt the ciphertext.

          cipherText = input("Enter the cipher text: ") # ask for the user to input ciphertext.

          Key1 = input("give the value of the key ") # ask the user to input the value of key.

          Key = int(Key1) # typecasting the value of the key.

          result = decrypt(cipherText, Key) # calling the decrypt function.

          return result

def decrypt(cipherText, Key): # the core function.
          
          result = "" #to store the value of result.

          matrix = [["" for x in range(len(cipherText))]for y in range(Key)] # a list of empty strings with rows equal to the value of key(main list) and columns equal to the length of the ciphertext(inner list dimensions).

          index = 0 # setting index value to 0.

          increment = 1 # setting increment value to 1.

          for selectedRow in range(0, len(matrix)): # for each selectedrow we set the value of row to 0.
                    row = 0

                    for col in range(0,len(matrix[row])): # for each column.
                            
                              if row+increment < 0 or row + increment >= len(matrix): # checking if we are going out of boundaries.
                                      
                                      increment = increment * -1 # if yes, then getting it back into the matrix. Eg: 1 -> -1, -1 -> 1.

                              if row == selectedRow: # or else, we check if value of row is equal to value of selectedRow
                                        matrix[row][col] += cipherText[index] # we go to the matrix and concatenate the ciphertext at that index.
                                        index += 1 # we increment the value of index.
                   
                              row += increment # we increment the value of row.
       
          matrix = transpose(matrix) # we call the transpose function.

          for list in matrix: # for each list in the tranposed matrix.
                    result += "".join(list) # we are picking each character in the transposed list of lists and concatenating to form a plaintext.
                    
          return result # return the result to the decrypt function.

def transpose(m): # function to transpose the matrix.

          result = [["" for y in range(len(m))]for x in range(len(m[0]))] # we are buidling a new reverse matrix.
          for i in range(len(m)): # for each position in the row
                    for j in range(len(m[0])): # for each position in the column
                              result[j][i]=m[i][j] # for each position of new matrix, we assign the value of the reversed matrix
          return result # return the result to the transpose function.
          
def main(): #main program
          print("Welcome to Rail Fence Cipher")
          cmd  = ''
          while cmd != '3': # Here we are giving to the user options, to encrypt, decrypt or quit. While the value of cmd is anything other than 3 finally block will be executed.
                    try:
                        cmd = input("[*] Common:\n1. Encryption\n2. Decryption\n3. Quit\n: ")
                        if cmd == '1':
                              print(encryption()) #if the user choose 1, encryption function is called.
                        if cmd == '2':
                              print(decryption()) #if the user chooses 2, decryption function is called.
                    except Exception as e:
                        print('[-] Wrong Input!\n' + str(e))
                    finally: #even if the try block doesn't execute, this block will be executed. 
                        print('\n' + '='*40)
                    print('='*10+"Thanks For Playing"+'='*10)
          
          
if __name__ == "__main__": #code to call the main function.
          main()
          
          
          
