SELECT pt_name, 
       pt_no,
       gend_cd,
       age,
       if(tlno is null, "NONE", tlno) tlno
from patient
where age <= 12 and gend_cd = "W"
order by age desc, pt_name