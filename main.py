# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:29:43 2021

@author: kalya
"""

import face_recognition,cv2,pickle
import enroll,spreadsheet,emailing,o_recognition


# recognition.load_facial_encodings_and_names_from_memory()

# spreadsheet.mark_all_absent()

# recognition.run_recognition()




enroll.enroll_via_camera('Nida')

#spreadsheet.enroll_person_to_sheet('Nida','nattaraut28@gmail.com')

#emailing.email_pin('nattaraut28@gmail.com',1234)