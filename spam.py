#Arigato#
import requests;print(requests.post('https://registrasi.tri.co.id/daftar/generateOTP?', 	data={'msisdn':input('[=] Nomer Target : ')}).json())