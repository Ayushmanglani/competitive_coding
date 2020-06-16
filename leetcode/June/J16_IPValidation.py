class Solution:
	def validIPAddress(self, IP: str) -> str:
		if ':' in IP:
			#ipv6 check
			a = IP.split(':')
			if len(a) != 8:
				return('Neither')
			for i in range(8):
				if not a[i] or len(a[i])>4 or '-' in a[i]:
					return('Neither')
				try:
					p = int(a[i], 16)
				except:
					return('Neither')
			return("IPv6")

		else:
			#ipv4 check
			a = IP.split('.')
			if len(a) != 4:
				return('Neither')
			for i in range(4):
				if not a[i] or len(str(a[i]))>3:
					return('Neither')
				try:
					if int(a[i])>255 or int(a[i])<0 or str(int(a[i])) != a[i]:
						return('Neither')
				except:
					return('Neither')
			return("IPv4")