import random

class Robot:
    def __init__(self, nama, nyawa, serangan):
        self.nama = nama
        self.nyawa = nyawa
        self.serangan = serangan
            
    def serang_musuh(self, musuh):
        if random.random() > 0.2:  # 80% kemungkinan berhasil
            damage = self.serangan
            musuh.nyawa -= damage
            print(f"{self.nama} menyerang {musuh.nama} dengan {damage} damage!")
        else:
            print(f"{self.nama} gagal menyerang {musuh.nama}!")
    
    def kalah(self):
        return self.nyawa <= 0

class Permainan:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
    
    def mulai(self):
        ronde = 1
        while not self.robot1.kalah() and not self.robot2.kalah():
            print(f"\n========================Ronde-{ronde} ==================================================")
            print(f"{self.robot1.nama} [{self.robot1.nyawa}|{self.robot1.serangan}]")
            print(f"{self.robot2.nama} [{self.robot2.nyawa}|{self.robot2.serangan}]")
            
            for robot, musuh in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:
                if robot.kalah():
                    continue
                print("\n1. Serang  2. Bertahan  3. Menyerah\n")
                aksi = int(input(f"{robot.nama}, silahkan pilih aksi: "))
                
                if aksi == 1:
                    robot.serang_musuh(musuh)
                elif aksi == 3:
                    print(f"{robot.nama} telah menyerah!")
                    return    
            ronde += 1
        if self.robot1.kalah():
            print(f"{self.robot2.nama} menang!")
        else:
            print(f"{self.robot1.nama} menang!")


nama1 = input("Masukkan nama robot pertama: ")
nama2 = input("Masukkan nama robot kedua: ")

robot1 = Robot(nama1, 650, 10)
robot2 = Robot(nama2, 750, 8)
permainan = Permainan(robot1, robot2)
permainan.mulai()
