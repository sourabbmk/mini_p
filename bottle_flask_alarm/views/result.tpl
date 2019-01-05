<!doctype html>
<html>
   <body>
   
      <table border = 1>
         %for key, value in result.items():
         
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
            
         %end
      </table>
      
   </body>
</html>