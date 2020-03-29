#!/usr/bin/env python

import speed, file, aws

def main():
 speeds = speed.speed_test()
 wfile = file.write_to(speeds)
 aws.putToS3(wfile)
 file.delete_file(wfile)

main()
