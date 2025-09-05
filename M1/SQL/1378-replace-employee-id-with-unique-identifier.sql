/*https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/ */

select unique_id, name from EmployeeUNI right join Employees on Employees.id = EmployeeUNI.id;