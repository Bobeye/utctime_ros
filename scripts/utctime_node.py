#!/usr/bin/env python
from std_msgs.msg import Time
import rospy
import datetime

pub = rospy.Publisher('utctime', Time, queue_size=1)

def setupPublisher():

	rospy.init_node('utctime_node', anonymous=True)
	rate = rospy.Rate(100) # 5hz

	while not rospy.is_shutdown():
		utc_datetime = datetime.datetime.utcnow()
		utc_gap = utc_datetime-datetime.datetime(1970,1,1)
		secs = int(utc_gap.total_seconds())
		nsecs = int((utc_gap.total_seconds()-secs)*1e9)
		t = rospy.Time(secs, nsecs)
		pub.publish(t)
		rate.sleep()

if __name__ == "__main__":
	 setupPublisher()