################################################################################
# Oracle Data Volume
################################################################################

resource "aws_ebs_volume" "oracle_data" {

  availability_zone = var.availability_zone

  size = 150

  type = "gp3"

  encrypted = true

  tags = merge(
    local.common_tags,
    {
      Name = "tinacloud-db01-data"
    }
  )

}

################################################################################
# Attach Volume
################################################################################

resource "aws_volume_attachment" "oracle_data" {

  device_name = "/dev/sdf"

  volume_id = aws_ebs_volume.oracle_data.id

  instance_id = aws_instance.tinacloud_db01.id

}