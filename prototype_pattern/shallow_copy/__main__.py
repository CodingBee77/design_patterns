from laptop import Laptop
from tower import Tower, MainBoard

l1 = Laptop("L1", "Intel", "32GB", "2TB SSD", "onboard", "1920x1080")
l1.display()
l2 = l1.clone()
l2.model = "L2"
l2.processor = "AMD"
l2.display()

