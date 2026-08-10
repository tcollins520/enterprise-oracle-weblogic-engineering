################################################################################
# Oracle Database Server (RHEL 8)
################################################################################

resource "aws_instance" "tinacloud_db01" {

  ami           = var.rhel_ami_id
  instance_type = var.database_instance_type

  key_name = aws_key_pair.tinacloud_bastion.key_name

  subnet_id = aws_subnet.private.id

  vpc_security_group_ids = [
    aws_security_group.oracle.id
  ]

  iam_instance_profile = aws_iam_instance_profile.oracle.name

  associate_public_ip_address = false

  monitoring = true

  user_data_replace_on_change = true

  user_data = file("${path.module}/userdata.sh")

  root_block_device {

    volume_size = 120
    volume_type = "gp3"
    encrypted   = true

    tags = merge(
      local.common_tags,
      {
        Name = "tinacloud-db01-root"
      }
    )

  }

  tags = merge(
    local.common_tags,
    {
      Name = "tinacloud-db01"
      Role = "Database"
      OS   = "RHEL8"
    }
  )

}

################################################################################
# Oracle WebLogic Application Server (RHEL 8)
################################################################################

resource "aws_instance" "tinacloud_app01" {

  ami           = var.rhel_ami_id
  instance_type = var.application_instance_type

  key_name = aws_key_pair.tinacloud_bastion.key_name

  subnet_id = aws_subnet.private.id

  vpc_security_group_ids = [
    aws_security_group.weblogic.id
  ]

  iam_instance_profile = aws_iam_instance_profile.oracle.name

  associate_public_ip_address = false

  monitoring = true

  user_data_replace_on_change = true

  user_data = file("${path.module}/userdata.sh")

  root_block_device {

    volume_size = 50
    volume_type = "gp3"
    encrypted   = true

    tags = merge(
      local.common_tags,
      {
        Name = "tinacloud-app01-root"
      }
    )

  }

  tags = merge(
    local.common_tags,
    {
      Name = "tinacloud-app01"
      Role = "Application"
      OS   = "RHEL8"
    }
  )

}